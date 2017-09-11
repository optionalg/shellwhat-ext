__version__ = '0.0.1'

def test_student_typed_all(state, text, msg="Submission does not contain the code `{}`.", spacer=None):
    """Test whether the student code contains multiple lines of text.

    Args:
        state : State instance describing student and solution code. Can be omitted if used with Ex().
        text  : List of regular expressions, one per student input line.
        msg   : Feedback message if text is not in student code.
        spacer: If not None, this character is replaced with r'\s+'. (Typically use '_' to make lines more readable.)

    :Example:
        If the student code is.. ::

            cd dental
            git add data/northern.csv
            git commit -m "Adding northern data."

        then the test could be:

            Ex().test_student_typed_all([r'cd_dental',
                                         r'git_add_data/northern.csv',
                                         r'git_commit_-m_"Adding_northern_data."'],
                                        msg="Use `cd`, `git add`, and `git commit`.",
                                        spacer='_')
    """

    if spacer is not None:
        text = [line.replace(spacer, r'\s+') for line in text]
    text = r'\s+' + '\n'.join(text) + r'\s+'
    return test_student_typed(state, text, msg, fixed=False)
