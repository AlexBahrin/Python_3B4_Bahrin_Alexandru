def build_xml_element(tag, content, **attrs):
    attr_str = ' '.join(f'{key}="{value}"' for key, value in attrs.items())
    return f'<{tag} {attr_str}>{content}</{tag}>'

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)