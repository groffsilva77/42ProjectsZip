/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ggroff-d <ggroff-d@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/11/09 15:01:44 by ggroff-d          #+#    #+#             */
/*   Updated: 2024/11/16 16:14:57 by ggroff-d         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static char	*ft_read_line(int fd)
{
	int		bytes_read;
	char	*buffer;

	buffer = malloc((BUFFER_SIZE + 1) * sizeof(char));
	if (!buffer)
		return (NULL);
	bytes_read = read(fd, buffer, BUFFER_SIZE);
	if (bytes_read == -1)
		return (free(buffer), NULL);
	buffer[bytes_read] = '\0';
	return (buffer);
}

static char	*ft_find_and_extract(char **buffer)
{
	char	*line;
	char	*newline_pos;
	char	*rest;

	if (!buffer || !*buffer || !**buffer)
		return (NULL);
	newline_pos = ft_strchr(*buffer, '\n');
	if (newline_pos)
	{
		line = ft_substr(*buffer, 0, newline_pos - *buffer + 1);
		if (!line)
			return (free(*buffer), *buffer = NULL, NULL);
		rest = ft_strdup(newline_pos + 1);
		if (!rest)
			return (free(line), free(*buffer), *buffer = NULL, NULL);
		free(*buffer);
		*buffer = rest;
	}
	else
	{
		line = ft_strdup(*buffer);
		free(*buffer);
		*buffer = NULL;
	}
	return (line);
}

static char	*ft_upbuffer(char *buffer, const char *temp)
{
	char	*new_buff;

	if (!temp)
		return (buffer);
	if (!buffer)
		return (ft_strdup(temp));
	new_buff = ft_strjoin(buffer, temp);
	if (!new_buff)
		return (free(buffer), NULL);
	free(buffer);
	return (new_buff);
}

char	*get_next_line(int fd)
{
	static char	*buffer;
	char		*temp;
	char		*line;

	if (fd < 0 || BUFFER_SIZE <= 0)
		return (NULL);
	while (!buffer || !ft_strchr(buffer, '\n'))
	{
		temp = ft_read_line(fd);
		if (!temp)
			return (free(buffer), buffer = NULL, NULL);
		if (!*temp)
		{
			free(temp);
			break ;
		}
		buffer = ft_upbuffer(buffer, temp);
		free(temp);
		if (!buffer)
			return (NULL);
	}
	line = ft_find_and_extract(&buffer);
	if (!line)
		return (free(buffer), buffer = NULL, NULL);
	return (line);
}
