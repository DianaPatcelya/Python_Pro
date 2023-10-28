def parse(query: str) -> dict:
    if '?' in query:
        query_params = query.split('?')[1]
        return {key_value_pair.split('=')[0]: key_value_pair.split('=')[1] for key_value_pair in query_params.split('&')
                if '=' in key_value_pair}
    else:
        return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=John') == {'name': 'John'}


def parse_cookie(query: str) -> dict:
    if query:
        cookie_pairs = query.split(';')
        return {pair.split('=', 1)[0]: pair.split('=', 1)[1] for pair in cookie_pairs if '=' in pair}
    else:
        return {}


if __name__ == '__main__':
    assert parse_cookie('name=John;') == {'name': 'John'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=John;age=28;') == {'name': 'John', 'age': '28'}
    assert parse_cookie('name=John=User;age=28;') == {'name': 'John=User', 'age': '28'}
