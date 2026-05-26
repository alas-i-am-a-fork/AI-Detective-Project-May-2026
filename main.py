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

            "Generate a COMPLETE detective case report.\n\n"

            "The report must include:\n"

            "1. Victim summary\n"
            "2. Chronological reconstruction of the crime\n"
            "3. Main suspects and motives\n"
            "4. Important evidence collected\n"
            "5. Contradictions or suspicious statements\n"
            "6. Step-by-step detective reasoning\n"
            "7. Why specific suspects became suspicious\n"
            "8. Why specific questions were asked\n"
            "9. Errors or interruptions during investigation\n"
            "10. Final conclusion\n\n"

            "Use the full investigation log.\n\n"

        )


        case_report = detective.analyze(
            "CASE REPORT SYSTEM",
            report_prompt
        )

        print(case_report)

        with open(
            "case_report.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write(case_report)

        print("\nCASE CLOSED.\n")
        print("Case report saved to case_report.txt")

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
