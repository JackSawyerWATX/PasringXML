import urllib.request
import xml.etree.ElementTree as ET

def extract_comments_and_sum(url):
    try:
        # Fetch the XML data from the URL
        response = urllib.request.urlopen(url)
        xml_data = response.read()

        # Parse the XML data using ElementTree
        tree = ET.fromstring(xml_data)

        # Find all the comment count elements
        comment_elements = tree.findall('.//comment/count')

        # Extract the comment counts and calculate the sum
        comment_sum = sum(int(comment.text) for comment in comment_elements)

        return comment_sum

    except Exception as e:
        print("An error occurred:", e)
        return None

def main():
    url =  ('http://py4e-data.dr-chuck.net/comments_1835495.xml')
    total_comments = extract_comments_and_sum(url)

    if total_comments is not None:
        print("Total comment counts:", total_comments)

if __name__ == "__main__":
    main()
