import os
import subprocess
import time

objectives = [
    "albuterol_similarity",
    "amlodipine_mpo",
    "celecoxib_rediscovery",
    "deco_hop",
    "drd2",
    "fexofenadine_mpo",
    "gsk3b",
    "isomers_c7h8n2o2",
    "isomers_c9h10n2o2pf2cl",
    "jnk3",
    "median1",
    "median2",
    "mestranol_similarity",
    "osimertinib_mpo",
    "perindopril_mpo",
    "qed",
    "ranolazine_mpo",
    "scaffold_hop",
    "sitagliptin_mpo",
    "thiothixene_rediscovery",
    "troglitazone_rediscovery",
    "zaleplon_mpo",
]


def run_gpu0():
    for i, obj in enumerate(objectives):

        # Run each experiment 3 times
        for run_id in range(1, 4):
            print(f"\n{'=' * 60}")
            print(f"TARGET {i + 1}/{len(objectives)}: {obj} | Run: {run_id}/3")
            print(f"{'=' * 60}\n")

            # Prepare environment
            env = os.environ.copy()
            env["PMO_OBJECTIVE"] = obj
            env["TARGET_GPU_ID"] = "0"
            env["PMO_RUN_ID"] = str(run_id)

            try:
                # Run main.py as a subprocess
                subprocess.run(["python", "main.py"], env=env, check=True)

            except subprocess.CalledProcessError as e:
                print(f"!! ERROR running {obj} (Run={run_id}) !!")
                print(e)
                # Optional: continue to next run
            except KeyboardInterrupt:
                print("\nBenchmark interrupted by user.")
                return

            # Small cooldown
            print(f"\nFinished run {run_id}. Cooling down for 5s...")
            time.sleep(5)


if __name__ == "__main__":
    run_gpu0()