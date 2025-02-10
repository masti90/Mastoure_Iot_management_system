'''

APM: salam arz shod



'''

from device import *
class AdminPanel:
    def __init__(self):
        self.groups = {}

    def create_group(self, group_name):
        if group_name not in self.groups:
            self.groups[group_name] = []
            print(f'groups {group_name} created')
        else:
            print('your group name is duplicated name')

    def add_device_to_group(self, group_name, device):
        if group_name in self.groups:
            self.groups[group_name].append(device)
            print(f'{device} added to group {group_name}')
        else:
            print(f'Group {group_name} does not exist')

    def create_device(self, group_name, device_type, name):
        if group_name in self.groups:
            topic = f'home/{group_name}/{device_type}/{name}'
            new_device = Device(topic)
            self.add_device_to_group(group_name, new_device)
            print(f'new device {new_device} created')
        else:
            print(f'Group {group_name} does not exist')

    def create_multiple_devices(self, group_name, device_type, number_of_devices):
        if group_name in self.groups:
            for i in range(1, number_of_devices + 1):
                device_name = f"{device_type}{i}"

                topic = f'home/{group_name}/{device_type}/{device_name.lower()}'

                new_device = Device(topic)

                self.add_device_to_group(group_name, new_device)
        else:
            print(f'Group {group_name} does not exist')

    def get_devices_in_groups(self, group_name):
        if group_name in self.groups:
            return self.groups[group_name]

        else:
            print(f'Group {group_name} does not exist')
            return []

    def turn_on_all_in_group(self, group_name):
        self.status = 'on'
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            #self.add_device_to_group(group_name, device)
            device.turn_on()
        print(f'all devices in {group_name} turned on')

    def turn_off_all_in_group(self, group_name):
        self.status = 'off'
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            #self.add_device_to_group(group_name, device)
            device.turn_off()
        print(f'all devices in {group_name} turned off')

    def turn_on_all(self):
        devices = self.get_devices_in_groups(group_name)
        for device in devices:
            self.add_device_to_group(group_name, device)
            device.turn_on()
            return f'all devices turned on'

    def turn_off_all(self):
        devices = self.get_devices_in_groups(self)
        for device in devices:
            device.turn_off()
            return f'all devices turned off'



    def get_status_in_group(self, group_name):
        #bebinid aval baayd bere too oon group_names betamame device ha dastresi peyda kone
        #ma yek tabe haminja darim bename  get_devices_in_groups(self, group_name): --> in bema yek list pas mide toosh koli device [d1,d2,d3,..]
        our_devices=self.get_device_in_groups(group_name) 

        #badesh vase done done devcie haye tooye in gorooh 
        #har kodom yek class az Device hastan --> yek tabe daran bename show status

        for i in our_devices:
            a=i.show_status()
            #hala print mikonim

            print(f'The device {i.name} is {a}')
#
#
#استاد لطفا راهنمایی کنید دیوانه شدم قاطی کردم این حل نمیشه
##
#
#
        '''living_room y matn print mikone mige lamp1 on , klamp2 off , lamp3 ,..'''
        pass

    def get_status_in_device_type(self, device_type):

        ''' device=lamps --> tamame lamp haro status mohem nabashe tooye living rome kojas'''
        pass

    def create_sensor(self):
        # bar asase clASS SENSOR argument bzarid
        pass

    def get_status_sensor_in_group(self, group_name):

        '''

        sensor haye yek goroh ro biad doone dooen status ro pas bde

        '''
        pass

if __name__ == '__main__':

    a1 = AdminPanel()
    a1.create_group('living_room')
    a1.create_group('bathroom')

    #a1.add_device_to_group('living_room', 'lamps' )
    #a1.add_device_to_group('kitchen', 'lamp3' )
    #a1.create_device('living_room', 'lamps', 'lamp1')
    a1.create_multiple_devices('living_room', 'lamps', 6)
    a1.create_multiple_devices('bathroom', 'fans', 2)
    print(a1.get_devices_in_groups('living_room'))
    print(a1.get_devices_in_groups('bathroom'))
    #print(a1.get_devices_in_groups('kitchen'))

    #mygroups = a1.groups['living_room']
    #print(mygroups[1].name)
    #print(mygroups[2].name)
    #print(mygroups[3].name)
    #print(mygroups[6].name)
    #mygroups[1].turn_on()
    a1.turn_on_all()
    #a1.turn_on_all_in_group('living_room')
    #a1.turn_off_all()
    #a1.turn_off_all_in_group('living_room')
