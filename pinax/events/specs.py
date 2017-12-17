from imagekit import ImageSpec
from pilkit.processors import ResizeToFit, SmartResize


class ImageThumbnail(ImageSpec):
    processors = [ResizeToFit(width=168, height=None)]
    format = "JPEG"
    options = {"quality": 75}


class SecondaryImageThumbnail(ImageSpec):
    processors = [SmartResize(405, 250)]
    format = "JPEG"
    options = {"quality": 75}
