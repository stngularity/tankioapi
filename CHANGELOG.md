## 1.0.1 `Backend update`
- `-` Removed `request_bytes` function
    > Changed to `request(bytes=True)` function

## 1.0.0
- `~` Rewrited use logic
    > Removed `TankiOnline` class. Now use function without this class

- `~` Rewrited docstrings for some functions
- `~` Fixed some mistakes in `MANIFEST.in`, `pyproject.toml` and `README.md`
    > For example, in `MANIFEST.in` was written `README.rst` instead of `README.md`

- `+` Added more useful functions
    > For example, in `GameObject` class, I added `read_image` function
 
- `+` Added `get_status` function
    > **Maybe deprecated!** Gets the status of stable game server

- `+` Added `get_test_status` function
    > Gets the status of test game servers

- `+` Added `py.typed`

## 1.0.0b1
- `~` Rewrited use logic
- `~` Rewrited docstrings for some functions
- `~` Fixed some mistakes in `MANIFEST.in`, `pyproject.toml` and `README.md`
- `+` Added more useful functions
- `+` Added `get_status` function
- `+` Added `py.typed`

## 0.1.0
- Initial release