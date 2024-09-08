from pydantic import BaseModel, Field


class ResourceMetadata(BaseModel):
    latin_name: str
    coords: str = Field(default="")
    foto_date: str = Field(default="")


class Resource(BaseModel):
    asset_id: str
    secure_url: str
    metadata: ResourceMetadata


class ResourceResponse(BaseModel):
    """
    Cloudinary API response.

    Response example:

    [{'asset_folder': 'animals_of_france',
                    'asset_id': 'd644784adaeab5fb5732544f47d1b76b',
                    'backup': True,
                    'bytes': 1430911,
                    'created_at': '2024-09-07T10:55:28Z',
                    'display_name': 'DSC_6142_kshfez',
                    'format': 'jpg',
                    'height': 1050,
                    'last_updated': {'metadata_updated_at': '2024-09-07T11:06:41+00:00',
                                     'tags_updated_at': '2024-09-07T12:00:58+00:00',
                                     'updated_at': '2024-09-07T12:00:58+00:00'},
                    'metadata': {'coords': '48.87316582228561, 2.2480885346790416',
                                 'foto_date': '2024-04-09',
                                 'latin_name': 'Ardea cinerea',
                                 'ru_name': 'Серая цапля'},
                    'public_id': 'DSC_6142_kshfez',
                    'resource_type': 'image',
                    'secure_url': 'https://res.cloudinary.com/cjkjvfnby/image/upload/v1725706528/DSC_6142_kshfez.jpg',
                    'type': 'upload',
                    'url': 'http://res.cloudinary.com/cjkjvfnby/image/upload/v1725706528/DSC_6142_kshfez.jpg',
                    'version': 1725706528,
                    'width': 1400},

    """

    resources: list[Resource]
