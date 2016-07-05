===============================
caixabreak
===============================


.. image:: https://img.shields.io/pypi/v/caixabreak.svg
        :target: https://pypi.python.org/pypi/caixabreak

.. image:: https://img.shields.io/travis/kintoandar/caixabreak.svg
        :target: https://travis-ci.org/kintoandar/caixabreak

.. image:: https://readthedocs.org/projects/caixabreak/badge/?version=latest
        :target: https://caixabreak.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/kintoandar/caixabreak/shield.svg
        :target: https://pyup.io/repos/github/kintoandar/caixabreak/
        :alt: Updates



* Free software: MIT license
* Documentation: https://caixabreak.readthedocs.io.
* Work in progress: New features will be available soon

About
--------

Extracts data from Caixa Geral de Depositos - Caixa Break management interface.

Install
--------

``pip install caixabreak``

Note: You must request the login credentials on a `CGD ATM machine first <https://www.cgd.pt/Particulares/Cartoes/Cartoes-Pre-pagos/Pages/Portal-pre-pagos.aspx>`_.

How-to
--------

``caixabreak --help``

::

    Usage: caixabreak [OPTIONS]

      Extracts data from CGD - Caixa Break management interface.

      Optional: Use environment variables instead of command line arguments
      (CGD_USER and CGD_PASS).

    Options:
      -u, --username TEXT  Access code for your account (7 digits)
      -p, --password TEXT  Password for your account (5 digits)
      -b, --balance        Show current balance
      -t, --transactions   Show current transactions
      --debug              Enable debug
      --help               Show this message and exit.

Features
--------

* Show current card balance
* Show table of transactions

Credits
---------

* `Joel Bastos <https://blog.kintoandar.com/>`_
* `André Ferreira <https://github.com/andreferreirav2/>`_


Disclamer
---------

This application is not affiliated with CGD in any way.
