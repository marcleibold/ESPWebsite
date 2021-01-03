def getControllersHTML(activeControllers):
    controllerHTML = ""
    if len(activeControllers) > 0:
        for esp in activeControllers:
            colorsHTML = ""
            for i, color in enumerate(esp['customColors']):
                colorsHTML += """<button id="%s_custom%d" class="customColor" style="background-color: %s;"></button>""" % (
                    esp['name'], i, color)

            controllerHTML += """
            <div class="controlsWrapper">
                        <div class="toprow">
                            <h1>%s</h1>
                            <label class="switch">
                            <input type="checkbox">
                            <span class="slider round"></span>
                        </label>
                        </div>
                        <div id="%s_picker" class="colorPicker"></div>
                        <h3 style="padding-bottom: 10px; border-bottom: 1px solid black;">Custom Colors</h3>
                        <div id="%s_custom" class="customColorWrapper">
                            %s
                            <button id="%s_addColor" class="customColor add">&#43</button>
                        </div>
                        <!-- custom Color Wrapper id will be {ESP Name} + _custom -->
                        <!-- custom Color id will be {ESP Name} + _custom + {custom_id} -->
                        <!-- add Color button id will be {ESP Name} + _addColor -->
                    </div>
                    <script type="text/javascript">
                        var colorPicker = new iro.ColorPicker("#%s_picker", {
                            width: 320,
                            color: "#fff",
                            borderColor: "#1d1d25",
                            borderWidth: 2
                        });
                    </script>
            """ % (esp['name'], esp['name'], esp['name'], colorsHTML, esp['name'], esp['name'])
    else:
        return ""
    return controllerHTML
