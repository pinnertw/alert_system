if [ ! $(pgrep -f alert:app) ]; then
	echo "start alert app"
	/home/pgi/miniconda3/envs/bybit/bin/python /home/pgi/miniconda3/envs/bybit/bin/uvicorn alert:app --reload
fi
