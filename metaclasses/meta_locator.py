class MetaLocator(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if isinstance(value, str):
                if value.startswith("//") or value.startswith(".//") or value.startswith("(//"):
                    # Преобразуем строку в локатор, если она начинается с '//' (XPath)
                    attrs[key] = ("xpath", value)
                elif value.startswith(".") or value.startswith("#"):
                    # Преобразуем строку в локатор, если она начинается с '.' или '#' (CSS селектор)
                    attrs[key] = ("css selector", value)
        return super().__new__(cls, name, bases, attrs)
