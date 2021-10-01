class Config:
    _conf = {
        "MQTT": {
            "broker": "192.168.178.73",
            "port": 31523,
            "client_id": "Main",
            "username": "",
            "password": ""
        }
    }

    @staticmethod
    def get(key: str):
        keys = key.split(".")
        if len(keys) == 0 or (len(keys) == 1 and len(keys[0]) == 0):
            raise AttributeError("You have to specify a key")
        res = Config._conf
        for i, k in enumerate(keys):
            try:
                res = res[k]
            except KeyError:
                prev = keys[i - 1] if i > 0 else "config"
                raise KeyError(f"Key '{k}' not present in '{prev}'")
        return res
