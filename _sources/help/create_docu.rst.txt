Create Documentation
==========================
This is a guide to create documentation for the project using Sphinx in VS Code. The following
steps will help you with the correct commands and workdflows in the template repository.

Requirements
------------
1. The repository is ready and all requirements are installed as explained here: :doc:`Start with repository <start_w_repo>`.

2. For simple local testing, I recommend installing an extension in VS Code. The extension is called **LiveServer** and can be found and installed directly in VS Code: https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer.

Customizing the documentation
-----------------------------
1. Placeholder 1

2. Change to the /docs directory
    Your path in the terminal looks like: **(.venv) D:\git\YouApp\src**

    .. code-block:: bash
        
        cd ../docs

3. Build html files
    Basic command for building html files

    .. code-block:: bash
        
        make html

    Previously delete the build directory and build html files

    .. code-block:: bash

        make clean && make html

    This command can be useful because dependencies or formatting from previous builds interfere with or destroy the view of new elements. So if the documentation looks strange for some unknown reason, this can be tried to solve it.

4. Start LiveServer
    To start the LiveServer, you have to open the index.html file in the build/html directory. Right-click on the index.html file and select **Open with Live Server**:
    
    .. image:: ../images/help_open_live_server.png
        :width: 400
        :alt: Setting shows start with LiveServer
