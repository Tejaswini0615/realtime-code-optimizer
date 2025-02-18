import cProfile, pstats, io

def profile_code(func, *args, **kwargs):
    profiler = cProfile.Profile()
    profiler.enable()
    result = func(*args, **kwargs)
    profiler.disable()
    
    stream = io.StringIO()
    stats = pstats.Stats(profiler, stream=stream)
    stats.strip_dirs().sort_stats('cumulative').print_stats(10)
    
    print(stream.getvalue())
    return result
