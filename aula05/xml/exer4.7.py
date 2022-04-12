from lxml import etree

def main():
    xml = etree.parse("conf.xml")
    root = xml.getroot()
    print(root.tag)
    printChild(root)

def printChild(root):
    for child in root:
        print(child.tag, child.attrib, child.text)
        printChild(child)

main()