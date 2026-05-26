from openai import OpenAI

from detectiveagent import DetectiveAgent


def main():

    try:

        # CONNECT TO OLLAMA
        ollama_client = OpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama"
        )

        detective = DetectiveAgent(
            model_client=ollama_client,
            model_name="mistral"
        )

        suspect_name = "Introduction"

        investigation_finished = False

        suspectnext = True

        print("DETECTIVE JADE HERE.\nWhat's your case?")

        statement = input(
            "Let's start with an introduction.\n\n"
        )

        analysis = detective.analyze(
            suspect_name,
            statement
        )

        print("\nDETECTIVE:")
        print(analysis)

        while not investigation_finished:

            if suspectnext:

                suspect_name = input(
                    "\nSUSPECT NAME: "
                )

                suspectnext = False

            statement = input(
                f"\n{suspect_name.upper()}:\n"
            )

            analysis = detective.analyze(
                suspect_name,
                statement
            )

            if "ERROR" in analysis:

                print(
                    "\nAn unexpected error occurred.\n"
                    "Apologies for the suddenness, "
                    "but it is time for me to go."
                )

                break

            print("\nDETECTIVE:")
            print(analysis)

            if "SUSPECT CHANGE" in analysis.upper():

                suspectnext = True

            if "CONFESSION" in analysis.upper():

                investigation_finished = True

        print("\nINVESTIGATION COMPLETE.")

        print("\nCASE REPORT")

        report_prompt = (
            "Generate a concise detective case report based on the "
            "entire investigation so far.\n\n"

            "Include:\n"
            "- victim summary\n"
            "- main suspects\n"
            "- important evidence\n"
            "- contradictions in testimony\n"
            "- likely sequence of events\n"
            "- most suspicious individual, your reasoning path\n"
            "- final conclusion\n\n"

            "Write formally, like an actual detective report."
        )

        case_report = detective.analyze(
            "CASE REPORT REQUEST",
            report_prompt
        )

        print(case_report)

        print("\nCASE CLOSED.")

    except KeyboardInterrupt:

        print(
            "\n\nInvestigation interrupted by user."
        )

    except Exception as e:

        print(
            "\nAn unexpected error occurred:"
        )

        print(e)


if __name__ == "__main__":

    main()
