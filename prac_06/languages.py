from prac_06.programming_language import ProgrammingLanguage


def main():

    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    #print(python)

    languages = [ruby, python, visual_basic]

    print(f"The dynamically typed languages are: ")
    dynamic_language = [language.name for language in languages if language.is_dynamic()]
    print(dynamic_language)
    for language in dynamic_language:
        print(language)

main()