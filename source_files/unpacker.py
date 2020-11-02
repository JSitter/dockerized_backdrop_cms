#!/usr/bin/env python3
from optparse import OptionParser
import os
from os import path
import tarfile
import shutil
import zipfile

temp_dir = '.tempdir'

def check_temp_dir():
    if not path.exists(temp_dir):
        os.mkdir(temp_dir)

def replace_item(source, destination):
    print("Source {}, dest {}".format(source, destination))
    if path.isdir(destination):
        remove_directory(destination)
    else:
        remove_file(destination)
    shutil.move(source, destination)

def unpack_file(temp_file_location, file, destination, replace=False):
    print("Unpack file function file {} desination {}".format(file, destination))
    file_destination = "{}/{}".format(destination, file)
    if not path.exists(file_destination):
        shutil.move("{}/{}".format(temp_file_location, file), destination)
    elif replace:
        replace_item("{}/{}".format(temp_file_location, file), "{}/{}".format(destination, file))
        print("Replaced {}.".format(file))
    else:
        print("Skipping {}. Already Exists. ".format(file))

def unpack_zip(source, destination):
    zipReference = zipfile.ZipFile(source, 'r')
    zipReference.extractall(destination)
    zipReference.close()
    print("Done")

def unpack_gz(source, destination):
    tarball = tarfile.open(source, 'r:gz')
    tarball.extractall(path=destination)
    print("Done")

def unpack_zip_into(source, destination, replace=False):
    print("Unpack zipinto source {} desination {}".format(source, destination))
    zipReference = zipfile.ZipFile(source, 'r')
    allfiles = zipReference.namelist()
    temp_source_dir = "{}/{}".format(temp_dir, allfiles[0][1])
    check_temp_dir()
    
    zipReference = zipfile.ZipFile(source, 'r')
    zipReference.extractall(path=temp_dir)
    files = os.listdir(temp_source_dir)

    for file in files:
        unpack_file(temp_source_dir, file, destination, replace)

    shutil.rmtree(temp_source_dir)
    
    zipReference.close()
    print("Done")

def unpack_gz_into(source, destination, replace=False):
    tar = tarfile.open(source, 'r:gz')
    allfiles = tar.getnames()
    temp_source_dir = "{}/{}".format(temp_dir, allfiles[0])

    if not path.exists(temp_dir):
        os.mkdir(temp_dir)
    
    tarball = tarfile.open(source, 'r:gz')
    tarball.extractall(path=temp_dir)
    files = os.listdir(temp_source_dir)

    for file in files:
        unpack_file(temp_source_dir, file, destination, replace)

    shutil.rmtree(temp_source_dir)
    print("Done")

def remove_file(source):
    print("remove file: {}".format(source))
    os.remove(source)

def remove_directory(source):
    print("Remove directory {}".format(source))
    shutil.rmtree(source)
    

if __name__ == "__main__":
    usage = "usage: %prog [options] zipped_package_location destination_package_location"
    parser = OptionParser(usage=usage)
    parser.add_option("-d",
                        help="Extract project into existing directory.",
                        action="store_true",
                        dest="directory",
                        default=False)

    parser.add_option("-r","--replace",
                    help="Replace existing files.",
                    action="store_true",
                    dest="replace",
                    default=False)

    (options, args) = parser.parse_args()
    home_directory = path.dirname(path.realpath(__file__))

    if len(args) > 1:
        if args[1][-1] == "/":
            final_project_path = home_directory+"/"+args[1][:-1]
        else:
            final_project_path = home_directory+"/"+args[1]
        zipped_project_path = home_directory+"/"+args[0]
    else:
        raise Exception("Error: 2 arguments required {} provided".format(len(args)-1))

    if not path.exists(zipped_project_path):
        raise Exception("Error: Zipped Project doesn't exist")

    ext = None
    if tarfile.is_tarfile(zipped_project_path):
        ext = "tar"
    elif zipfile.is_zipfile(zipped_project_path):
        ext = "zip"
    else:
        raise Exception("Error: Unknown project file format. Must be zip or gz")
    if options.directory:
        if not path.exists(final_project_path):
            raise Exception("Error: Destination directory does not exist.")

    if options.directory:
        if ext == "zip":
            unpack_zip_into(zipped_project_path, final_project_path, options.replace)
        else:
            unpack_gz_into(zipped_project_path, final_project_path, options.replace)
    else:
        if ext == "zip":
            unpack_zip(zipped_project_path, final_project_path)
        else:
            unpack_gz(zipped_project_path, final_project_path)
