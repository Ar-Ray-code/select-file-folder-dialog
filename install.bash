SCRIPT_DIR=$(cd $(dirname $0); pwd)

## UNINSTALL =============================================
if [ "uninstall" = $1 ]; then
    echo "uninstall ..."
    ## REMOVE FILE
    rm -rf /usr/local/bin/select-file-folder-dialog.py
    exit 0

## INSTALL =============================================

elif [ "install" = $1 ]; then
    cp -r $SCRIPT_DIR/select-file-folder-dialog.py /usr/local/bin/
else
    ## ERROR MESSAGE
    echo "options failed ('sudo bash ./install.bash install' or 'sudo bash ./install.bash uninstall')"
    exit 1
fi
