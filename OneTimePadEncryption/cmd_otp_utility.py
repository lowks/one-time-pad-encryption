#!/usr/bin/env python2.7
__author__ = 'marcsantiago'
import argparse
from OneTimePadEncryption import OneTimePadEncryption

opt = OneTimePadEncryption.OneTimePadEncryption()

parser = argparse.ArgumentParser(description='One Time Pad Encryption Software')
parser.add_argument('-e',  '--encrypt_string', help='Encrypts a string that the user has entered' )
parser.add_argument('-d',  '--decrypt_string', help='Decrypts a string. User must also key provided a key')
parser.add_argument('-k',  '--key',            help='User enters the key as a string')
parser.add_argument('-kf',  '--key_file',      help='User enters the key file path')
parser.add_argument('-ef', '--encrypt_file',   help='Encrypts file data')
parser.add_argument('-df', '--decrypt_file',   help='Decrypts data from file. key can be from file or string.')

args = vars(parser.parse_args())

if args['encrypt_string']:
    opt.encrypt_string_or_file(args['encrypt_string'], string_file_mode=False)

elif args['encrypt_file']:
    opt.encrypt_string_or_file(args['encrypt_file'], string_file_mode=True)

elif args['decrypt_string'] and args['key_file']:
    opt.decrypt_string_or_file(args['key_file'], args['decrypt_string'], key_file_mode=True, encrypted_string_file_mode=False)

elif args['decrypt_string'] and args['key']:
    opt.decrypt_string_or_file(args['key'], args['decrypt_string'], key_file_mode=False, encrypted_string_file_mode=False)

elif args['decrypt_file'] and args['key_file']:
    opt.decrypt_string_or_file(args['key_file'], args['decrypt_file'], key_file_mode=True, encrypted_string_file_mode=True)

elif args['decrypt_file'] and args['key']:
    opt.decrypt_string_or_file(args['key'], args['decrypt_file'], key_file_mode=False, encrypted_string_file_mode=True)


