class NoExtensionException(Exception):
    def __init__(self, e_name, *args, **kwargs):
        super(NoExtensionException, self).__init__(
            'No {} extension found'.format(e_name)
        )


class BlueprintException(Exception):
    pass
