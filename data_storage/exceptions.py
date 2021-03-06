class ResourceAlreadyExist(Exception):
    pass

class ResourceNotFound(Exception):
    pass

class MetaMetadataMissing(Exception):
    def __init__(self,resourcename,blob_path):
        super().__init__("The meta metadata file({1}) for resource({0}) is missing.".format(resourcename,blob_path))

