class SecurityLevel:
    levels = ["Unclassified", "Confidential", "Secret", "Top Secret"]
    
    @staticmethod
    def get_level_index(level):
        if level in SecurityLevel.levels:
            return SecurityLevel.levels.index(level)
        raise ValueError("Invalid security level")

class Subject:
    def __init__(self, name, security_level):
        self.name = name
        self.security_level = security_level

class Object:
    def __init__(self, name, security_level, content=""):
        self.name = name
        self.security_level = security_level
        self.content = content

class BellLaPadulaSystem:
    def __init__(self):
        self.subjects = {}
        self.objects = {}

    def add_subject(self, name, security_level):
        if name in self.subjects:
            raise ValueError("Subject already exists")
        self.subjects[name] = Subject(name, security_level)

    def add_object(self, name, security_level, content=""):
        if name in self.objects:
            raise ValueError("Object already exists")
        self.objects[name] = Object(name, security_level, content)

    def read(self, subject_name, object_name):
        if subject_name not in self.subjects or object_name not in self.objects:
            return "Error: Subject or Object does not exist"

        subject = self.subjects[subject_name]
        obj = self.objects[object_name]

        if SecurityLevel.get_level_index(subject.security_level) >= SecurityLevel.get_level_index(obj.security_level):
            return f"{subject.name} reads {obj.name}: {obj.content}"
        else:
            return f"ACCESS DENIED: {subject.name} cannot read {obj.name} (No Read Up)"

    def write(self, subject_name, object_name, content):
        if subject_name not in self.subjects or object_name not in self.objects:
            return "Error: Subject or Object does not exist"

        subject = self.subjects[subject_name]
        obj = self.objects[object_name]

        if SecurityLevel.get_level_index(subject.security_level) <= SecurityLevel.get_level_index(obj.security_level):
            obj.content = content
            return f"{subject.name} writes to {obj.name}: {content}"
        else:
            return f"ACCESS DENIED: {subject.name} cannot write to {obj.name} (No Write Down)"

# Example Usage
blp_system = BellLaPadulaSystem()
blp_system.add_subject("Alice", "Secret")
blp_system.add_subject("Bob", "Confidential")
blp_system.add_object("File1", "Confidential", "This is confidential data.")
blp_system.add_object("File2", "Secret", "This is secret data.")

# Testing
print(blp_system.read("Alice", "File1"))  # Allowed (Secret >= Confidential)
print(blp_system.read("Bob", "File2"))    # Denied (Confidential < Secret)
print(blp_system.write("Alice", "File1", "Updated Data"))  # Denied (No Write Down)
print(blp_system.write("Bob", "File1", "New Confidential Data"))  # Allowed
