from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .models import File


def file_upload_function(instance: "File", filename: str) -> str:
    """
    This function is used to generate the path for the file to be uploaded to.

    Args:
        instance: The instance of the FileModel.
        filename: The name of the file.

    Returns:
        The path to upload the file to.
    """

    folder = instance.parent_folder
    upload_path = f"{folder.path}/{folder.name}/{filename}"

    return upload_path
