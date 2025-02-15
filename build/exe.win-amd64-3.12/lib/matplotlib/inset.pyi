from . import artist
from .axes import Axes
from .backend_bases import RendererBase
from .patches import ConnectionPatch, Rectangle

from .typing import ColorType, LineStyleType

class InsetIndicator(artist.Artist):
    def __init__(
        self,
        bounds: tuple[float, float, float, float] | None = ...,
        inset_ax: Axes | None = ...,
        zorder: float | None = ...,
        **kwargs
    ) -> None: ...
    def set_alpha(self, alpha: float | None) -> None: ...
    def set_edgecolor(self, color: ColorType | None) -> None: ...
    def set_color(self, c: ColorType | None) -> None: ...
    def set_linewidth(self, w: float | None) -> None: ...
    def set_linestyle(self, ls: LineStyleType | None) -> None: ...
    @property
    def rectangle(self) -> Rectangle: ...
    @property
    def connectors(self) -> tuple[ConnectionPatch, ConnectionPatch, ConnectionPatch, ConnectionPatch] | None: ...
    def draw(self, renderer: RendererBase) -> None: ...
