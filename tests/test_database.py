import numpy as np

from unittest import TestCase
from ezyrb import Database


class TestDatabase(TestCase):
    def test_constructor_empty(self):
        a = Database()

    def test_constructor_arg(self):
        Database(np.random.uniform(size=(10, 3)),
                 np.random.uniform(size=(10, 8)))

    def test_constructor_arg_wrong(self):
        with self.assertRaises(ValueError):
            Database(np.random.uniform(size=(9, 3)),
                     np.random.uniform(size=(10, 8)))

    def test_constructor_error(self):
        with self.assertRaises(TypeError):
            Database(np.eye(5))

    def test_getitem(self):
        org = Database(np.random.uniform(size=(10, 3)),
                       np.random.uniform(size=(10, 8)))
        new = org[2::2]
        assert new.parameters_matrix.shape[0] == new.snapshots_matrix.shape[0] == 4
    
    def test_getitem_singular(self): 
        org = Database(np.random.uniform(size=(10, 3)),
                       np.random.uniform(size=(10, 8)))
        new = org[2]
        assert True

    def test_matrices(self):
        org = Database(np.random.uniform(size=(10, 3)),
                       np.random.uniform(size=(10, 8)))
        assert org.parameters_matrix.shape == (10, 3)
        assert org.snapshots_matrix.shape == (10, 8)

    # def test_split(self):
    #     org = Database(np.random.uniform(size=(10, 3)),
    #                    np.random.uniform(size=(10, 8)))
    #     t1, t2 = org.split([8, 2])
    #     print(t1)
    #     assert False