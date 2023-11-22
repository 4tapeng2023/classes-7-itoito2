from unittest import TestCase, mock, main
from xml_file_processor import FileProcessor

class TestXMLFileProcessor(TestCase):
    def test_read_file(self) -> None:
        ...


    @mock.patch('xml_file_processor.read_file')
    def test_read_file_mock(self, mock_method) -> None:
        FP = FileProcessor()
        mock_method.return_value = {"id": "10", "name": "Chopper", "bounty":" 100"}
        file_data = FP.read_file('file.xml')
        self.assertEqual({"id": "10", "name": "Chopper", "bounty":" 100"}, file_data)

if __name__ == '__main__':
    main()
