for /R "d:\Ryesim\Calibration_example" %%g in (.) do (
pushd %%g
echo now in %%g
grid1.bat
popd
)
