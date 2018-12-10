######################################################
# Author: Andrea Fioraldi <andreafioraldi@gmail.com> #
# License: BSD 2-Clause                              #
######################################################

import manage

print "######### IDAngr GUI #########"

def show():
    if not manage.is_initialized():
        from init_gui import IDAngrConnectDialog
        if IDAngrConnectDialog.go():
            from main_gui import idangr_panel_show
            idangr_panel_show()
    else:
        from main_gui import idangr_panel_show
        idangr_panel_show()
