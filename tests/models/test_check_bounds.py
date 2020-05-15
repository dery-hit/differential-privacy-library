from unittest import TestCase

from diffprivlib.models.utils import _check_bounds


class TestGaussianNB(TestCase):
    def test_none(self):
        self.assertIsNone(_check_bounds(None))

    def test_non_list(self):
        with self.assertRaises(TypeError):
            _check_bounds((1, 2, 3))

    def test_incorrect_entries(self):
        with self.assertRaises(ValueError):
            _check_bounds([(1, 2, 3)])

        with self.assertRaises(ValueError):
            _check_bounds([(1,)])

    def test_consistency(self):
        bounds = _check_bounds([(1, 2), (4, 5)], dims=2)
        bounds2 = _check_bounds(bounds, dims=2)
        self.assertEqual(bounds, bounds2)

    def test_tuple_output(self):
        bounds = _check_bounds([[1, 2]])
        self.assertIsInstance(bounds[0], tuple)

    def test_wrong_dims(self):
        with self.assertRaises(ValueError):
            _check_bounds([(1, 2)], dims=2)

    def test_wrong_order(self):
        with self.assertRaises(ValueError):
            _check_bounds([(2, 1)])

    def test_non_numeric(self):
        with self.assertRaises(TypeError):
            _check_bounds([("1", "2")])

    def test_min_separation(self):
        bounds = _check_bounds([(1, 1)], min_separation=1)
        self.assertEqual((0.5, 1.5), bounds[0])
