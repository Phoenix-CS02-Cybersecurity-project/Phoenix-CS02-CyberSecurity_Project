#!usr\bin\env python
import subprocess
import optparse

def change(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest = "interface", help = "INTERFACE TO CHANGE")
parser.add_option("-m","--new_mac", dest = "new_mac", help = "NEW MAC ADDRESS")

(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

change(interface, new_mac);

