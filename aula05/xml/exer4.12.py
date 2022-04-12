from lxml import etree

def main():
    doc = etree.parse("playlist.xspf")

    schema = etree.parse("xspf-1_0.7.rng")
    validator = etree.RelaxNG(schema)

    root = etree.Element("validator")
    valid = etree.SubElement(root, "valid")
    valid.text = str(validator.validate(doc))
    error = etree.SubElement(root, "error")
    error.text = validator.error_log.last_error.message

    print(etree.tostring(root, pretty_print=True).decode())

main()