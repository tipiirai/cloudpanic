1. Install pip, virtualenv & virtualenvwrapper:

        sudo easy_install pip
        sudo easy_install virtualenv
        sudo pip install virtualenvwrapper

    Note where pip installs virtualenvwrapper.

2. Add the following two lines to your shell startup file(`~/.bash_profile` for example).
        
        export WORKON_HOME=~/.virtualenv
        mkdir -p $WORKON_HOME
        source </usr/local/bin>/virtualenvwrapper.sh

    Ensure that the `virtualenvwrapper.sh` file is prefixed with the path noted in step 1.

3. Clone this repository

        git clone git@github.com:tipiirai/cloudpanic.git

4. Switch to the `refactor` branch

5. Update submodules

        git submodule init
        git submodule update

6. Setup your [virtual environment](http://www.doughellmann.com/docs/virtualenvwrapper/)

        mkvirtualenv cp

    You can use `workon cp` to switch to the environment after the first time.

6. Install the requirements:

        cd ~/path/to/this/repo
        pip install -r requirements.txt