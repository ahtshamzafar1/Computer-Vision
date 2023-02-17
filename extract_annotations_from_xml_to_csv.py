import os
import xml.etree.ElementTree as ET
import csv

# set the folder containing the XML files
folder_path = "folder"

# create a list of all XML files in the folder
xml_files = [f for f in os.listdir(folder_path) if f.endswith('.xml')]

# loop through all XML files and extract the annotations
annotations = []
for file in xml_files:
    # parse the XML file
    tree = ET.parse(os.path.join(folder_path, file))
    root = tree.getroot()

    # extract the image filename
    filename = root.find('filename').text

    # loop through all objects in the file and extract their attributes
    for obj in root.iter('object'):
        name = obj.find('name').text
        bbox = obj.find('bndbox')
        xmin = int(bbox.find('xmin').text)
        ymin = int(bbox.find('ymin').text)
        xmax = int(bbox.find('xmax').text)
        ymax = int(bbox.find('ymax').text)

        # optionally, extract additional attributes such as pose or truncated
        pose = obj.find('pose').text if obj.find('pose') is not None else ''
        truncated = obj.find('truncated').text if obj.find('truncated') is not None else ''
        difficult = obj.find('difficult').text if obj.find('difficult') is not None else ''

        # add the annotation to the list
        annotations.append([filename, name, xmin, ymin, xmax, ymax, pose, truncated, difficult])

# write the annotations to a CSV file
with open('annotations.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['filename', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'pose', 'truncated', 'difficult'])
    writer.writerows(annotations)
