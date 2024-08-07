import yaml, os, subprocess
#from generators.generateInventory import generateInventory, getFabricName
#from generators.generateCVPDeploymentPlaybook import generateCVPDeploymentPlaybook
#from generators.generateGroupVarsAll import generateGroupVarsAll
#from generators.generateGroupVarsCVP import generateGroupVarsCVP
#from generators.generateGroupVarsFabric import generateGroupVarsFabric
#from generators.generateGroupVarsSpines import generateGroupVarsSpines
#from generators.generateGroupVarsL3Leafs import generateGroupVarsL3Leafs
#from generators.generateGroupVarsL2Leafs import generateGroupVarsL2Leafs
#from generators.generateGroupVarsTenants import generateGroupVarsTenants
from generators.generateGroupVarsServers import generateGroupVarsServers

import argparse
#from getpass import getpass

def main():
    parser = argparse.ArgumentParser(
        description='Creates necessary files to run Arista AVD ansible playbook')
    parser.add_argument('-f', '--file', help="path to Excel file")
    args = parser.parse_args()

#    cvpadmin_password = getpass("cvpadmin password: ")
    # confirm_password = getpass("Confirm cvpadmin password: ")
    # if cvpadmin_password != confirm_password:
    #     print("Passwords do not match")
    #     return

    file_location = args.file
    if file_location is None:
        print("Please specify a path for the Excel file by using -f. Enter 'python main.py -h' for more details.")
        return
#    fabric_name = getFabricName(file_location)
    avd = {
    "inventory": None,
    "group_vars": {
#        "all": None,
#        "CVP": None,
#        fabric_name: None,
#        "SPINES": None,
##        "L3_LEAFS": None,
#        "L2_LEAFS": None,
#        "TENANT_NETWORKS": None,
        "DC1_SERVERS": None
        },
#    "dc-fabric-deploy-cvp": None,
#    "dc-fabric-post-validation": None,
#    "requirements": None,
    }
#    avd["requirements"] = '''ansible==2.9.2
#netaddr==0.7.19
#Jinja2==2.10.3
#requests==2.22.0
#treelib==1.5.5
#pytest==5.3.4
#pytest-html
#ward==0.34.0b0
#git+https://github.com/batfish/pybatfish.git
#cvprac==1.0.4'''
#    avd["inventory"] = generateInventory(file_location)
#    avd["dc-fabric-deploy-cvp"] = generateCVPDeploymentPlaybook(file_location)
#   avd["group_vars"]["all"] = generateGroupVarsAll(file_location)
##    avd["group_vars"]["CVP"] = generateGroupVarsCVP(file_location, cvpadmin_password)
#    avd["group_vars"][fabric_name] = generateGroupVarsFabric(file_location)
#    avd["group_vars"]["SPINES"] = generateGroupVarsSpines(file_location)
#    avd["group_vars"]["L3_LEAFS"] = generateGroupVarsL3Leafs(file_location)
#    avd["group_vars"]["L2_LEAFS"] = generateGroupVarsL2Leafs(file_location)
#    avd["group_vars"]["TENANT_NETWORKS"] = generateGroupVarsTenants(file_location)
    avd["inventory"]["group_vars"]["DC1_SERVERS"] = generateGroupVarsServers(file_location)

    #Create avd directory
#    if not os.path.exists("./avd"):
#        os.mkdir("./avd")
#        os.mkdir("./avd/collections")

    ##Install ansible collections if necessary
    #if not os.path.exists("./avd/collections/ansible_collections/arista/avd"):
    #    print("Installing arista.avd collection")
    #    process = subprocess.Popen(['ansible-galaxy', 'collection', 'install', 'arista.avd', '-p', './avd/collections'],
    #                 stdout=subprocess.PIPE, 
    #                 stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()
    #if not os.path.exists("./avd/collections/ansible_collections/arista/cvp"):
    #    print("Installing arista.cvp collection")
    #    process = subprocess.Popen(['ansible-galaxy', 'collection', 'install', 'arista.cvp',  '-p', './avd/collections'],
    #                 stdout=subprocess.PIPE, 
    #                 stderr=subprocess.PIPE)
    #    stdout, stderr = process.communicate()
#
    ##Create intended directories
    #if not os.path.exists("./avd/intended/batfish"):
    #    os.makedirs("./avd/intended/batfish")
    #if not os.path.exists("./avd/intended/configs"):
    #    os.makedirs("./avd/intended/configs")
    #if not os.path.exists("./avd/intended/structured_configs"):
    #    os.makedirs("./avd/intended/structured_configs")
    #if not os.path.exists("./avd/intended/structured_configs/cvp"):
    #    os.makedirs("./avd/intended/structured_configs/cvp")

    ##Create documentation directory
    #if not os.path.exists("./avd/documentation/{}".format(fabric_name)):
    #    os.makedirs("./avd/documentation/{}".format(fabric_name))
    #if not os.path.exists("./avd/documentation/devices"):
    #    os.makedirs("./avd/documentation/devices")
#
    ##Create inventory file
    #with open("./avd/inventory.yml", "w") as inv:
    #    inv.write(yaml.dump(avd["inventory"]))

    #Create group_vars files
#   if not os.path.exists("./avd/group_vars"):
#       os.mkdir("./avd/group_vars")
    for k, v in avd["group_vars"].items():
        path = "./group_vars/{}.yml".format(k)
        with open(path, "w") as gvfile:
            gvfile.write(yaml.dump(v))

    ##Create ansible config file
    #from ansible_config import ansible_config
    #with open("./avd/ansible.cfg", "w") as ans_cfg:
    #    ans_cfg.write(ansible_config)
    #
    ##Create dc-fabric-deploy-cvp.yml
    #with open("./avd/dc-fabric-deploy-cvp.yml", "w") as ans_pb:
    #    ans_pb.write(avd["dc-fabric-deploy-cvp"])
#
    ##Create requirements file
    #with open("./avd/requirements.txt", "w") as reqs:
    #    reqs.write(avd["requirements"])

    #Install requirements
    #process = subprocess.Popen(['pip', 'install', '-r', './avd/requirements.txt'],
    #                 stdout=subprocess.PIPE, 
    #                 stderr=subprocess.PIPE)
    #stdout, stderr = process.communicate()

    #Create dc-fabric-post-validation.yml

if __name__ == "__main__":
    main()
