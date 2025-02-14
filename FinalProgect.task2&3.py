from mypyc.build import group_name

from datetime import datetime

from device import *

class AdminPanel:

    def __init__(self):

        self.groups = {}



    def create_group(self, group_name):

        if group_name not in self.groups:

            self.groups[group_name] = []

            print(f"groups {group_name} created")

        else:

            print("your group name is duplicated name")



    def add_device_to_group(self, group_name, device):

        if group_name in self.groups:

            self.groups[group_name].append(device)

            print(f"{device} added to group {group_name}")

        else:

            print(f"Group {group_name} does not exist")



    def create_device(self, group_name, device_type, name):

        if group_name in self.groups:

            topic = f"home/{group_name}/{device_type}/{name}"

            new_device = Device(topic)

            self.add_device_to_group(group_name, new_device)

            print(f"new device {new_device} created")

        else:

            print(f"Group {group_name} does not exist")



    def create_multiple_devices(self, group_name, device_type, number_of_devices):

        if group_name in self.groups:

            for i in range(1, number_of_devices + 1):

                device_name = f"{device_type}{i}"



                topic = f"home/{group_name}/{device_type}/{device_name.lower()}"



                new_device = Device(topic)



                self.add_device_to_group(group_name, new_device)

        else:

            print(f"Group {group_name} does not exist")



    def get_devices_in_groups(self, group_name):

        if group_name in self.groups:

            return self.groups[group_name]



        else:

            print(f"Groupeee {group_name} does not exist")

            return []



    def turn_on_all_in_group(self, group_name):

        self.status = "on"

        devices = self.get_devices_in_groups(group_name)

        for device in devices:

            device.turn_on()

        print(f"all devices in {group_name} turned on")



    def turn_off_all_in_group(self, group_name):

        self.status = "off"

        devices = self.get_devices_in_groups(group_name)

        for device in devices:

            device.turn_off()

        print(f"all devices in {group_name} turned off")



    def turn_on_all(self):

        devices = self.get_devices_in_groups(self)

        for device in devices:



            device.turn_on()

            return f"all devices turned on"



    def turn_off_all(self):

        devices = self.get_devices_in_groups(self)

        for device in devices:

            device.turn_off()

            return f"all devices turned off"



    def get_status_in_group(self, group_name):

        if group_name in self.groups:

            device_name = self.get_devices_in_groups(group_name)[1]



            j = device_name.get_status()

            print(f"The device {device_name} is {j}")



        else:

            print(f"Group {group_name} does not exist")



    def get_status_in_device_type(self, device_type):

        if device_type in self.groups:

            device_type = self.get_devices_in_groups(group_name)[1]

            return device_type

            print(f"Device type {device_type} is in group {group_name}")



        else:

            print(f"Device type {device_type} does not exist")



    def create_sensor(self, group_name, sensor_type, name, pin):

        if group_name in self.groups:

            topic = f"home/{group_name}/{sensor_type}/{name}"

            new_device = Sensor(topic, pin)

            self.add_device_to_group(group_name, new_device)

            print(f"new device {new_device} created")

        else:

            print(f"Group {group_name} does not exist")



    def get_status_sensor_in_group(self, group_name):

        if group_name in self.groups:

            for sensor in self.get_devices_in_groups(group_name):

                if sensor is Sensor:

                    device_name = sensor.name

                    j = sensor.read_sensor()

                    print(f"Sensor {device_name} status is {j}")



        else:

            print(f"Group {group_name} does not exist")


    def day_or_night(self):

        hour = datetime.now().hour

        return "Day" if 6 <= hour < 18 else "Night"







if __name__ == "__main__":



    a1 = AdminPanel()

    a1.create_group("living_room")

    a1.create_group("bathroom")



    # a1.add_device_to_group('living_room', 'lamps' )

    # a1.add_device_to_group('kitchen', 'lamp3' )

    # a1.create_device('living_room', 'lamps', 'lamp1')

    a1.create_multiple_devices("living_room", "lamps", 6)

    a1.create_multiple_devices("bathroom", "fans", 2)

    print(a1.get_devices_in_groups("living_room"))

    print(a1.get_devices_in_groups("bathroom"))

    # print(a1.get_devices_in_groups('kitchen'))



    # mygroups = a1.groups['living_room']

    # print(mygroups[1].name)

    # print(mygroups[2].name)

    # print(mygroups[3].name)

    # print(mygroups[6].name)

    # mygroups[1].turn_on()



    a1.turn_on_all_in_group("living_room")



    # a1.turn_off_all_in_group('living_room')



    # a1.get_status_in_group('living_room')

    # a1.get_status_in_group('bathroom')



    # a1.get_status_in_device_type('fans')

