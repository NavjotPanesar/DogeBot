pluginList = ["ExplicitMemeGen","Parrot","ImplicitMemeGen", "Buzzwords"]

class plugin_classes:
    from plugin_parrot import Parrot
    from plugin_meme_gen import ExplicitMemeGen
    from plugin_meme_gen import ImplicitMemeGen
    from plugin_buzzwords import Buzzwords

    all_commands = None
    @staticmethod
    def get_commands_list():
        return plugin_classes.get_command_to_plugin_map().keys()

    command_to_plugin_mapping = None
    @staticmethod
    def get_command_to_plugin_map():
        if plugin_classes.command_to_plugin_mapping is None:
            plugin_classes.command_to_plugin_mapping = dict()
            for pluginName in pluginList:
                pluginClass = getattr(plugin_classes, pluginName)
                plugin = pluginClass()
                for plugin_command in plugin.registered_commands:
                    plugin_classes.command_to_plugin_mapping[plugin_command] = plugin
        return plugin_classes.command_to_plugin_mapping
