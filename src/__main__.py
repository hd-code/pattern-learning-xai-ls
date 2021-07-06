"""Executes the app."""

import logging
import traceback

from app import App


app = App()

try:
    app.init()
    app.run()
except Exception:
    logging.error(traceback.format_exc())
except:
    print("An unknown error occurred")
finally:
    app.exit()
