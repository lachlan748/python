from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
from pprint import pprint

if __name__ == '__main__':
    inventory_file_name = './hosts.yml'
    data_loader = DataLoader()
    inventory = InventoryManager(loader = data_loader, sources = [inventory_file_name])
    variable_manager = VariableManager(loader = data_loader, inventory = inventory)
    pprint(inventory.get_groups_dict()['all'])
    pprint(inventory.list_hosts())
    pprint(variable_manager.get_vars())
    data = inventory.get_groups_dict()
    pprint(data)
