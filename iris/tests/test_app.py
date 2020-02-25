from iris.app import app
import unittest

class TestModel(unittest.TestCase):

    def setUp(self):
        app.testing = True

    def tearDown(self):
        return super().tearDown()

    def test_model(self):
        prediction = '2'
        data = {
            'sepal_length': 1,
            'sepal_width': 1,
            'petal_length': 1,
            'petal_width': 1
        }
        with app.test_client() as c:
            r = c.post('/api/v1/predict', data=data)
            p = r.json.get('prediction')
            self.assertEqual(prediction, p)


if __name__ == '__main__':
    unittest.main()
