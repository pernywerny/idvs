# messages are session messages
# initialization =  messages.add_message(request, messages.*message_type*, *message_text*)
# message types(levels) are: DEBUG(will not work in production), INFO, SUCCESS, WARNING, ERROR
# eg. messages.add_message(request, messages.ERROR, 'Input Validation Failed)
# could also be added using messages.*message_type*(request, *message_text*)

from django.contrib import messages


class MessageController:
    exc = None
    exceptionMessage = f'A fatal error: {exc} has occurred. Please contact GPF-ITD if this problem persists'
    loginMsg = 'Please Login to complete that action'
    
    def setErrorMessage(self, request, message):
        if message:
            if message != "":
                messages.error(request, message)

    def setSuccessMessage(self, request, message):
        if message:
            if request:
                if message != "":
                    messages.success(request, message)

    def setInfoMessage(request, message):
        if message:
            if request:
                if message != "":
                    messages.info(request, message)

    def setWarningMessage(request, message):
        if message:
            if request:
                if message != "":
                    messages.warning(request, f"Warning: {message}")
