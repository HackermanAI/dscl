
	                   ___           ___                   
	    _____         /\__\         /\__\                  
	   /::\  \       /:/ _/_       /:/  /                  
	  /:/\:\  \     /:/ /\  \     /:/  /                   
	 /:/  \:\__\   /:/ /::\  \   /:/  /  ___   ___     ___ 
	/:/__/ \:|__| /:/_/:/\:\__\ /:/__/  /\__\ /\  \   /\__\
	\:\  \ /:/  / \:\/:/ /:/  / \:\  \ /:/  / \:\  \ /:/  /
	 \:\  /:/  /   \::/ /:/  /   \:\  /:/  /   \:\  /:/  / 
	  \:\/:/  /     \/_/:/  /     \:\/:/  /     \:\/:/  /  
	   \::/  /        /:/  /       \::/  /       \::/  /   
	    \/__/         \/__/         \/__/         \/__/    
	
	              Dead Simple Config Lang


## Example usage:

	from dscl import dscl
	config = dscl.parse(path_to_config_file)

## Example config-file syntax:

	[plugins]

	syntax_highlighter      true                  -- enable or disable syntax highlighting plugin
	git_integration         true                  -- enable or disable git integration
	auto_complete           true                  -- enable or disable auto completion

	[themes]

	current_theme           "monokai"             -- set the active theme
	theme_path              "~/.config/themes"    -- path where custom themes are stored

	[logs]

	log_level               "info"                -- set the log level (debug, info, warn, error)
	log_file                "/var/log/editor.log" -- location to store logs

	@module                                       -- import module
