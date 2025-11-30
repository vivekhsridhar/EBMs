import importlib, sys
modules = ['numpy','matplotlib','keras','tensorflow']
for m in modules:
    try:
        mod = importlib.import_module(m)
        v = getattr(mod, '__version__', 'unknown')
        print(f"{m}: {v}")
    except Exception as e:
        print(f"{m}: import failed: {e}")
        sys.exit(1)
print('IMPORT_CHECK_OK')
