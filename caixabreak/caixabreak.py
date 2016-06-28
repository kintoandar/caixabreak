#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import requests
import sys
import logging
from lxml import html

"""As the CGD page structure might change, this global config should make it easier to adapt."""
_config = {
    'base_url': 'https://portalprepagos.cgd.pt/portalprepagos/',
    'welcome_page': 'login.seam?sp_param=PrePago',
    'welcome_credentials': {
        'USERNAME': '1234567',
        'login_btn_1PPP': 'OK'
    },
    'login_page': 'auth/forms/login.fcc',
    'management_page': 'private/saldoMovimentos.seam',
    'login_credentials': {
        'target': '/portalprepagos/private/home.seam',
        'username': 'PPP1234567',
        'userInput': '1234567',
        'passwordInput': '*****',
        'loginForm:submit': 'Entrar',
        'password': '12345'
    },
    'xpath': {
        'current_balance': '//*[@id="consultaMovimentosCartoesPrePagos"]/div[4]/div/div/div/div/p[2]/label[1]/text()'
    }
}

"""Setup logging using standard error and level as WARNING."""
logging.basicConfig(stream=sys.stderr,
                    level=logging.WARNING,
                    format='%(levelname)s:%(asctime)s:%(message)s')


def get_html_tree():
    """Gets and converts the management interface page into a parsable tree."""
    try:
        with requests.Session() as s:
            s = requests.Session()
            s.get(_config['base_url'] + _config['welcome_page'],
                  data=_config['welcome_credentials'])

            logging.debug('GET {0}'.format(_config['base_url'] +
                          _config['welcome_page']))

            s.post(_config['base_url'] + _config['login_page'],
                   data=_config['login_credentials'])

            logging.debug('POST {0}'.format(_config['base_url'] +
                          _config['login_page']))

            r = s.get(_config['base_url'] + _config['management_page'])

            logging.debug('GET {0}'.format(_config['base_url'] +
                          _config['login_page']))
    except Exception as e:
        raise e
    return html.fromstring(r.content)


def current_balance(tree):
    """Extracts the current balance from the html tree structure.

    :param tree: The HTML page
    """
    try:
        balance = tree.xpath(_config['xpath']['current_balance'])[0].strip()
    except Exception as e:
        raise e
    return balance


@click.command()
@click.option('--username', envvar='CGD_USER', prompt=True,
              help='Access code for your account (7 digits)')
@click.option('--password', envvar='CGD_PASS', prompt=True, hide_input=True,
              help='Password for your account (5 digits)')
def main(username, password):
    """Extracts data from ``CGD - Caixa Break`` management interface.

    Optional: Use environment variables instead of command line arguments (CGD_USER and CGD_PASS).
    """

    global _config
    _config['welcome_credentials']['USERNAME'] = username
    _config['login_credentials']['username'] = 'PPP' + username
    _config['login_credentials']['userInput'] = username
    _config['login_credentials']['password'] = password

    try:
        tree = get_html_tree()
        click.echo('Current balance: {0}€'.format(current_balance(tree)))
    except Exception as e:
        logging.error(e)
        sys.exit(1)

if __name__ == '__main__':
    main()
