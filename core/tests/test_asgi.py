# python
import os
import sys
import types
import importlib
import unittest

class ASGITests(unittest.TestCase):
    def setUp(self):
        # backup any existing django modules and fusion.asgi
        self._backups = {name: sys.modules.get(name) for name in ('django', 'django.core', 'django.core.asgi', 'fusion.asgi')}
        # ensure fresh import
        sys.modules.pop('fusion.asgi', None)

    def tearDown(self):
        # restore backups
        for name, module in self._backups.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module
        # cleanup env var
        os.environ.pop('DJANGO_SETTINGS_MODULE', None)

    def _inject_fake_asgi(self, return_value_or_callable):
        """
        Create minimal fake packages:
         - django
         - django.core
         - django.core.asgi with get_asgi_application
        """
        django = types.ModuleType('django')
        core = types.ModuleType('django.core')
        asgi_mod = types.ModuleType('django.core.asgi')

        def get_asgi_application():
            return return_value_or_callable

        asgi_mod.get_asgi_application = get_asgi_application
        core.asgi = asgi_mod
        django.core = core

        sys.modules['django'] = django
        sys.modules['django.core'] = core
        sys.modules['django.core.asgi'] = asgi_mod

    def test_sets_default_django_settings_when_missing(self):
        os.environ.pop('DJANGO_SETTINGS_MODULE', None)
        sentinel = object()
        self._inject_fake_asgi(sentinel)

        mod = importlib.import_module('fusion.asgi')

        self.assertEqual(os.environ.get('DJANGO_SETTINGS_MODULE'), 'fusion.settings')
        self.assertIs(mod.application, sentinel)

    def test_respects_existing_django_settings(self):
        os.environ['DJANGO_SETTINGS_MODULE'] = 'custom.settings'
        sentinel = object()
        self._inject_fake_asgi(sentinel)

        mod = importlib.import_module('fusion.asgi')

        self.assertEqual(os.environ.get('DJANGO_SETTINGS_MODULE'), 'custom.settings')
        self.assertIs(mod.application, sentinel)

    def test_get_asgi_application_called_once_and_returns_callable(self):
        os.environ.pop('DJANGO_SETTINGS_MODULE', None)
        calls = []
        def fake_factory():
            calls.append(True)
            return lambda scope, receive, send: None

        self._inject_fake_asgi(fake_factory)

        mod = importlib.import_module('fusion.asgi')

        self.assertEqual(len(calls), 0)
        self.assertTrue(callable(mod.application))

if __name__ == '__main__':
    unittest.main()
