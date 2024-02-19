class SerializerTestBase:
    """
    Base class for testing serializers.

    This class should be inherited by all serializer test cases and
    expects the following attributes to be set:
    - serializer_class: The serializer class that should be tested
    - search_key: The key that should be used to search for the
        database entry

    This class does not implement a setup method. The child class
    should implement this method and set the following attributes:
    - self.data: The data that should be used for testing
    - self.serializer: The serializer instance that should be
        tested
    """

    # Set the serializer class that should be used
    # this should be set in the child class
    serializer_class = None
    search_key = None

    @classmethod
    def setUpClass(cls):
        """Check if the child class has set the required attributes."""
        if cls.serializer_class is None:
            raise NotImplementedError("The serializer_class attribute must be set.")
        if cls.search_key is None:
            raise NotImplementedError("The search_key attribute must be set.")

    def test_attributes(self):
        """Test if the serializer has the correct attributes."""
        self.serializer = self.serializer_class(data=self.input_data)
        self.serializer.is_valid(raise_exception=True)
        serial_data = self.serializer.data
        # self.assertEqual(serial_data.keys(), self.data.keys())

        for key in self.expected_data.keys():
            self.assertEqual(
                serial_data[key],
                self.expected_data[key],
                "Attribute {} is not correct, expected {}, got {}".format(
                    key, self.expected_data[key], serial_data[key]
                ),
            )

    def test_create(self):
        """Test if the serializer can create a new database entry."""
        # Delete the model from the database
        search_kwargs = {self.search_key: self.input_data[self.search_key]}
        self.serializer_class.Meta.model.objects.filter(**search_kwargs).delete()

        self.serializer = self.serializer_class(data=self.input_data)
        self.serializer.is_valid(raise_exception=True)
        self.serializer.create(self.input_data)
        self.assertTrue(self.serializer.Meta.model.objects.filter(**search_kwargs).exists())
