import numpy as np
import numpy.testing as npt
import pytest
from cadastro import ad_pessoa


def test_cadastro_ad_pessoa():
    "Check the result"
    computed = ad_pessoa.add_one(4.2)
    reference = 5.2
    npt.assert_almost_equal(computed, reference, decimal=12)
