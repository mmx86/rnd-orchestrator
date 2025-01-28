import functools
import typing

import fastapi
import dsp


@functools.lru_cache
def settings() -> dsp.settings.Settings:
    return dsp.settings.Settings()


SettingsDep = typing.Annotated[dsp.settings.Settings, fastapi.Depends(settings)]
