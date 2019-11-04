from screenpy.abilities.browse_the_web import BrowseTheWeb
from screenpy.actor import Actor
from screenpy.pacing import beat, aside, MINOR
from screenpy.target import Target

class Clear:

    """
    Clears the text from an input field. A Clear action is expected to be
    instantiated by its static |Clear.the_text_from| method. A typical
    invocation might look like:
        Clear.the_text_from(COMMENT_FIELD)
    It can then be passed along to the |Actor| to perform the action.
    """

    @beat("{0} clears text from {target}.", gravitas=MINOR)
    def perform_as(self, the_actor: Actor) -> None:
        """
        Asks the |Actor| to performs the Clear action, Clearing the text
        from the targeted input field using their ability to
        |BrowseTheWeb|.
        Args:
            the_actor: The |Actor| who will perform this action.
        Raises:
            |UnableToPerformException|: if the actor does not have the
                ability to |BrowseTheWeb|.
        """
        element = self.target.found_by(the_actor)
        element.clear()

    @staticmethod
    def the_text_from(target: Target) -> "Clear":
        """
        Creates a new Clear action with the provided text. It is expected
        that the next call will be to the instantiated Clear object's
        |Clear.the_text_from| method.

        Args:
            target (Target): the |Target| from which to clear the text.

        Returns:
            |Clear|
        """
        return Clear(target)

    @staticmethod
    def the_text_from_the(target: Target) -> "Clear":
        """Syntactic sugar for |Clear.the_text_from|."""
        return Clear.the_text_from(target)

    def __init__(self, target: Target) -> "Clear":
        self.target = target